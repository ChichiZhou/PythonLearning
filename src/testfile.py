import pytest

def writetoafile(fname):
    with open(fname, 'w') as fp:
        fp.write('Hello\n')

def test_writetofile(tmpdir):
    file = tmpdir.join('output.txt')
    writetoafile(file.strpath)  # or use str(file)
    assert file.read() == 'Hello\n'


if __name__ == '__main__':
    pytest.main(["testfile.py"])

