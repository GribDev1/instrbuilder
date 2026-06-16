from pathlib import Path
from instrbuilder import instrument_opening

csv_dir = Path.cwd() / "instrbuilder" / "instruments"
instrument_opening.init_yaml(csv_dir=str(csv_dir))