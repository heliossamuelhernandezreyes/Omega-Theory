from pathlib import Path
import subprocess, sys
import pandas as pd

def test_regenerate_01_06(tmp_path: Path):
    script=Path(__file__).resolve().parents[1]/'scripts'/'regenerate_deliveries_01_06.py'
    subprocess.run([sys.executable,str(script),'--output',str(tmp_path)],check=True)
    c=pd.read_csv(tmp_path/'d01_continuity.csv')
    assert int(c.loc[c.epsilon==0,'components'].iloc[0])==2
    assert (c.loc[c.epsilon>0,'components']==1).all()
    r=pd.read_csv(tmp_path/'d02_relabel.csv')
    assert float(r.absolute_difference.iloc[0])<1e-12
    s=pd.read_csv(tmp_path/'d03_survival.csv')
    assert float(s.abs_error.max())<1e-14
    m=pd.read_csv(tmp_path/'d04_memory.csv')
    assert m.monotonic_non_decreasing.all()
    t=pd.read_csv(tmp_path/'d05_trajectories.csv')
    assert float(t.max_relative_drift.max())<1e-8
    assert float(t.max_abs_speed.max())<1
    f=pd.read_csv(tmp_path/'d06_profiles.csv')
    assert float((f.field_power+2).abs().max())<1e-10
