config = {
    "scheduler_config": {
        "gpu": ["0", "1", "2"], # if you want to use clusters of gpus, refer to the original repo
        "force_rerun":True,     # when initially setiing up, this code is required to prevent your scheduler from "skipping" tasks, refer to the original github
        "result_root_folder":'gpuscheduler/results', # generate a seperate directory to not make your folder messy :(
        "temp_folder ":'gpuscheduler/temp',
        "scheduler_log_file_path":'gpuscheduler/scheduler.log'
    },

    "test_config": [
        {
            "arg1": ["a", "b", "c"], # where your parameters(for argument parsing) should go
            "arg2": ["d", "e", "f"],
            "arg3": [True]
        }
    ]
}
