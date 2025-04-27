# freetv-web-automation


## 🚀 Getting Started

In order to start the automation process,  
clone the code using the command below:
## 🚀 Getting Started

In order to start the automation process,  
clone the code using the command below:

```bash
git clone https://github.com/boris-sionov/grafana_automation_project.git
```


## 📦 Install Dependencies

After cloning the project, install the required packages using:
```bash
cd configuration
pip install -r requirements.txt
```

Install Browsers:
```bash
python -m playwright install
```



## ⚙️ Configure Settings

After installing dependencies, make sure to update the `config.ini` file with the correct values:

```ini
[web]
url = 

[general]
platform = 

[account]
; Add phone number, first and last name
phone_number = 
first_name = 
last_name = 
```

Choose Browser to run the test:
Open `pytest.ini` file and choose your desired browser (Chromium, Firefox, Webkit)
```ini
[pytest]
--browser=chromium
```