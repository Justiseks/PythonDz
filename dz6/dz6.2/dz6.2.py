import pytest
from dz62function import merge_and_write

@pytest.fixture
def setup_files(tmpdir):
    file1_content = "Word"
    file2_content = "Fish"
    file1_path = tmpdir.join("file1.txt")
    file2_path = tmpdir.join("file2.txt")
    file1_path.write(file1_content)
    file2_path.write(file2_content)
    return str(file1_path), str(file2_path)

def testing_write(setup_files, tmpdir):
    file1_path, file2_path = setup_files
    output_file_path = tmpdir.join("output.txt")
    expected_data = "Word Fish"
    result = merge_and_write(file1_path, file2_path, str(output_file_path))
    assert os.path.exists(str(output_file_path))
    assert result == expected_data

def testing_not_found(tmpdir):
    file1_path = tmpdir.join("nonexistent_file.txt")
    file2_path = tmpdir.join("file2.txt")
    output_file_path = tmpdir.join("output.txt")
    result = merge_and_write(str(file1_path), str(file2_path), str(output_file_path))
    assert result == "Один из файлов не найден"
