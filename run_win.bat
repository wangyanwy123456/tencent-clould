pytest --alluredir report
allure generate report -c -o report/html
allure open report/html