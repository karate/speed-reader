Install tk (for arch linux, run `pacman -S tk`)

```bash
# enter project directory
cd speed-reader
# activate virtuelenv
virtualenv .
source bin/activate
# install dependencies
pip install -r requirements.txt
# run the program
python reader.py lotr-intro.txt
```
