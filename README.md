# fico-estimator

Fico-estimator is a ML model for estimating fico scores using the interest rate of an applicants recent loan. The library provides a guestimate instead of having to request a credit check. It is trained using 8,000 loans from Lending Clubs Marketplace and normalized to exclude any changes in the Federal Reserve prime rate. The library also includes a scraper for collecting new training data for experiment with the model. Predicted scores are within 70 points of accuracy. 
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
from fico-estimator import Estimator

fe = Estimator()
#get a fico estimate
fe.predict(rate)

#get lending club loan data from marketplace
fe.scrape(html)

#improve the modeling by training it with external data
fe.train(data)

```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
