import pytest
from log_reader import CSVLogAdapter, JSONLogAdapter, LogReader
from analysis_config import AnalysisConfigBuilder
from detection import AnalysisContext, FailureBurstStrategy, FailureThenSuccessStrategy
from incident import Incident

@pytest.mark.parametrize('adapter,path,count', [(CSVLogAdapter(),'data/sample.csv',3),(JSONLogAdapter(),'data/sample.json',2)])
def test_read(adapter,path,count):
    assert isinstance(adapter,LogReader)
    assert len(adapter.read_logs(path)) == count

def test_missing(tmp_path):
    p = tmp_path/'bad.csv'; p.write_text('username,result\na,failure\n')
    with pytest.raises(ValueError,match='timestamp'): CSVLogAdapter().read_logs(p)

@pytest.mark.parametrize('value',[0,-1,1.5])
def test_builder(value):
    with pytest.raises(ValueError): AnalysisConfigBuilder().with_threshold(value).build()

@pytest.mark.parametrize('strategy',[FailureBurstStrategy(),FailureThenSuccessStrategy()])
def test_detection(strategy):
    records = CSVLogAdapter().read_logs('data/sample.csv') + JSONLogAdapter().read_logs('data/sample.json')
    assert len(AnalysisContext(strategy).analyze(records,AnalysisConfigBuilder().build())) == 1
    assert not AnalysisContext(strategy).analyze(records,AnalysisConfigBuilder().with_window(1).build())
    assert not AnalysisContext(strategy).analyze(records,AnalysisConfigBuilder().with_ip('192.0.2.9').build())

def test_state():
    e = Incident('test','192.0.2.1',None)
    assert e.status == 'Yeni'
    with pytest.raises(ValueError): e.resolve()
    e.investigate(); assert e.status == 'İnceleniyor'
    e.resolve(); assert e.status == 'Çözüldü'
    with pytest.raises(ValueError): e.investigate()
