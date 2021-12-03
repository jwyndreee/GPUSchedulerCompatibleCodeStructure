# modify your usual code like this

def parse_args(additional_args):
    parser = argparse.ArgumentParser(description='', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--arg1', type=str, default='a', help='a|b|c')
    parser.add_argument('--arg2', type=str, default='d', help='d|e|f')
    parser.add_argument('--arg3', action='store_true', help='')
    
    if additional_args == None:
        args = parser.parse_args()
    else:
        args = parser.parse_args('')
        for k, v in additional_args.items():
            setattr(args, k, v)
    return args
    
def main(additional_args = None):
    args = parse_args(additional_args)
    return

from gpu_task_scheduler.gpu_task import GPUTask

class Task(GPUTask):
    def main(self):
        main(self._config)
        
if __name__ == '__main__':
    main()
