import os
cmd = "php artisan serve --host=127.0.0.1 --port=8000"

returned_value = os.system(cmd)  # returns the exit code in unix
print('returned value:', returned_value)
