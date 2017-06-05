## To install:
Go to http://www.lfd.uci.edu/~gohlke/pythonlibs/

Download:
 * Numpy (numpy-1.13.0rc1+mkl-cp34-cp34m-win32.whl)
 * Scipy (scipy-0.19.0-cp34-cp34m-win32.whl)
 * Scikit Learn (scikit_learn-0.18.1-cp34-cp34m-win32.whl)

```
pip install C:\Users\Eyokiha\Downloads\numpy-1.13.0rc1+mkl-cp34-cp34m-win32.whl
pip install C:\Users\Eyokiha\Downloads\scipy-0.19.0-cp34-cp34m-win32.whl
pip install C:\Users\Eyokiha\Downloads\scikit_learn-0.18.1-cp34-cp34m-win32.whl
```

The Kickstarter_2017-02-15T22_22_48_377Z.json file was downloaded from https://webrobots.io/kickstarter-datasets/ (or get the zip from: https://www.dropbox.com/s/x7bs4v0nr4vy10n/Kickstarter_2017-02-15T22_22_48_377Z.zip?dl=0)


Follow the following steps to get the Spearman correlation results and the F-score:

```
Input                                                             >   Python file                  >   Output
-------------------------------------------------------------------------------------------------------------------------------------------------------------
Kickstarter_2017-02-15T22_22_48_377Z - Copy.json                  >   parsedataset.py              >   webrobot_dataset_parsed.txt
webrobot_dataset_parsed.txt                                       >   description_text_spider.py   >   ks_scraped_data.jl
webrobot_dataset_parsed.txt + ks_scraped_data.jl                  >   parseoutput_kNN.py           >   combiOutput.txt
ks_scraped_data.jl                                                >   getAllTexts.py               >   allText[i].txt
allText[i].txt                                                    >   LIWC                         >   LIWC2015 Results (TXT files (1000 files)).txt
combiOutput.txt + LIWC2015 Results (TXT files (1000 files)).txt   >   combineWithLIWC.py           >   LIWC_Combi.txt

LIWC_Combi.txt                                                    >   SPSS                         >   Spearman correlation results
combiOutput.txt                                                   >   kNN.py                       >   F-score
```