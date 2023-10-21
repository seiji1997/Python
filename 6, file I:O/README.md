# Python
Become a Python master

### Google Drive 

mount on Google Drive
```python
from google.colab import drive
drive.mount('/content/drive')
```

created data(df) of shape .csv using pandas output to Google Drive
```python
df.to_csv('/content/drive/My Drive/output.csv', index=False)
```

