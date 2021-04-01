# fico-estimator

Fico-estimator is a Python library for estimating fico scores using an interest rate.
It is trained using 8,000 loans from Lending Clubs Marketplace and normalized to exclude any changes in the Federal Reserve prime rate. The library also includes a scraper for collecting new loan data to further training and experiment by adding other variables to the regression. Predicted scores are within 50 points of accuracy. 
## Installation

Use the package manager [pip] Only compatable with python 2.7
```bash
pip install fico-estimator
```

## Dependencies
```
import sklearn
import BeautifulSoup
import numpy
import pandas
```

## Usage

```python
import fico-estimator as fe

#get a fico estimate
fe.predict_fico(rate)

#train using the new data. Returns regression intercept and coeficient (y = mx + b)
fe.train(data)

#get lending club loan data from marketplace
fe.scrape(html)
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
