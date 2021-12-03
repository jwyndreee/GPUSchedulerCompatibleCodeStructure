# modify your usual code like this

def parse_args(additional_args):
    parser = argparse.ArgumentParser(description='', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--arg1', type=str, default='a', help='a|b|c')
    parser.add_argument('--arg2', type=str, default='d', help='d|e|f')
    parser.add_argument('--arg3', action='store_true', help='')
    parser.add_argument('--arg4', type=str, default='d', help='d|e|f')
    parser.add_argument('--arg5', type=str, default='d', help='d|e|f')
    parser.add_argument('--arg6', type=str, default='d', help='d|e|f')
    
    if additional_args == None:
        args = parser.parse_args() # if run with main.py, argument parsing works as before
    else:
        args = parser.parse_args('') # if run with main_schedule.py '' ensures all arguments to be initialized with their default values
        for k, v in additional_args.items(): # after that the to-be-tuned experimental arguments are overridden with additional_args
            setattr(args, k, v) # origin of additional_args can be found in Line:28, self._config
    return args
    
def main(additional_args = None):
    args = parse_args(additional_args)
    # followed with your regular code to init & train & eval
    return

from gpu_task_scheduler.gpu_task import GPUTask
class Task(GPUTask):
    def main(self):
        main(self._config)
        
if __name__ == '__main__':
    main()
