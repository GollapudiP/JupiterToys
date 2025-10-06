# Web Application Automation with Selenium, Python and Robot Framework

This repository contains a structured automation framework using:

- Selenium WebDriver  
- Python 
- Robot Framework
- DataDriver
- GitHub Actions for Continuous Integration
  
---

## Technologies Used

- Python 3.13.7
- Robot Framework 7.3.2
- Robot Framework Selenium Library 6.3.0
- Robot Framework Data Driver 1.11.2

---

## Installation & Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/GollapudiP/JupiterToys.git
   cd JupiterToys
   
2. **Install Dependencies**
   ```bash
   python -m pip install --upgrade pip
   pip install -r requirements.txt

3. **Execute Tests**
   ```bash
   robot -d results/ .

This will:

- Read test data from CSV file under TestData/
- Launch Chrome browser
- The execution HTML report will be saved as an artifact in the GitHub Actions workflow runs
- Use GitHub Actions workflow to run tests on a scheduled run daily.
  
---

## Best Practices

- Use DataDriver for test reusability
- Structure POM classes cleanly (1 page = 1 class)
- Integrate with GitHub Actions CI pipelines.

---

## License

MIT © 2025 Priyanka Gollapudi

---

## Author

Priyanka Gollapudi
