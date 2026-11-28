import argparse
from pathlib import Path
from datetime import datetime
from log_reader import CSVLogAdapter, JSONLogAdapter
from analysis_config import AnalysisConfigBuilder
from detection import AnalysisContext, FailureBurstStrategy, FailureThenSuccessStrategy

def main():
    p = argparse.ArgumentParser(description='Security log analysis')
    p.add_argument('files', nargs='*', default=[str(Path(__file__).parent / 'data' / n) for n in ('sample.csv','sample.json')])
    p.add_argument('--threshold', type=int, default=3)
    p.add_argument('--window', type=int, default=300)
    p.add_argument('--ip')
    p.add_argument('--start', type=datetime.fromisoformat)
    p.add_argument('--end', type=datetime.fromisoformat)
    p.add_argument('--method', choices=['burst','success','both'], default='both')
    p.add_argument('--interactive', action='store_true')
    args = p.parse_args()
    try:
        config = AnalysisConfigBuilder().with_threshold(args.threshold).with_window(args.window).with_ip(args.ip).with_period(args.start,args.end).with_method(args.method).build()
        records = []
        for file in args.files:
            adapters = {'.csv': CSVLogAdapter, '.json': JSONLogAdapter}
            suffix = Path(file).suffix.lower()
            if suffix not in adapters: raise ValueError('Unsupported file type')
            records.extend(adapters[suffix]().read_logs(file))
        strategies = {'burst': FailureBurstStrategy(), 'success': FailureThenSuccessStrategy()}
        incidents = []
        for name, strategy in strategies.items():
            if config.method in (name,'both'): incidents.extend(AnalysisContext(strategy).analyze(records,config))
        print(f'{len(records)} records, {len(incidents)} incidents')
        for i, event in enumerate(incidents,1):
            print(i,event.kind,event.ip_address,event.timestamp,event.status)
        if args.interactive:
            while True:
                command = input('Incident number + investigate/resolve, or q: ').strip()
                if command == 'q': break
                try:
                    number, action = command.split()
                    index = int(number)-1
                    if not 0 <= index < len(incidents): raise ValueError('Invalid incident number')
                    event = incidents[index]
                    if action == 'investigate': event.investigate()
                    elif action == 'resolve': event.resolve()
                    else: raise ValueError('Unknown action')
                    print(event.status)
                except ValueError as e: print(e)
    except (OSError, ValueError, TypeError) as e: p.exit(1, f'Error: {e}\n')

if __name__ == '__main__': main()
