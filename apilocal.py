import os
cmd = "php artisan serve --port=9000"

returned_value = os.system(cmd)  # returns the exit code in unix
print('returned value:', returned_value)
