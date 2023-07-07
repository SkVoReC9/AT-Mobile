# Mobile Autotests

# Install requirements
```
pip Install -r requirements.txt
```

# Run all Autotests
```
pytest ./Tests/
```

# Run Single Autotests
```
pytest ./Tests/%test_name%
```

# Run Autotests with Allure
```
pytest ./Tests/  --aluredir=%pathToDir%
```

# Run Autotests with unique IP
```
pytest ./Tests/  --alluredir=%pathToDir% --host_appium=%YourIp%
```
