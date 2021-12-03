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
            "no_debug": [True], # where your parameters(for argument parsing) should go
            "multi_scale": [True],
            "multi_scale_recon": [True],
            "ms_fw_ver": [4, 5, 6],
            "tqdm_off": [True],
        }
    ]
}
