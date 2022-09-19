import datetime, json


def logger(file_path= "my_log.log"):
    def logger_(func):
        def new_func(*args, **kwargs):
            call_time = datetime.datetime.now()
            result = func(*args, **kwargs)
            log = {
                "date": str(call_time.date()),
                "time": str(call_time.time()),
                "function_name": str(func.__name__),
                "param_list": args,
                "param_dict": kwargs,
                "result": result
            }
            with open(file_path, "a") as file:
                json.dump(log, file, sort_keys=False)
                file.write("\n")
            return result
        return new_func
    return logger_