from bmi_calc import get_weight_category_count, build_dataframe

json_path = './bmi.json'
csv_path = './table1.csv'

completed_dataframe = build_dataframe(json_path, csv_path)


def test_build_dataframe():
    assert 'BMI' in completed_dataframe.columns
    assert 'BMI Category' in completed_dataframe.columns
    assert 'Health Risk' in completed_dataframe.columns


def test_build_dataframe2():
    assert len(list(completed_dataframe.BMI)) == 6


def test_build_dataframe3():
    assert type(list(completed_dataframe.BMI)[0]) == float


def test_build_dataframe4():
    assert type(completed_dataframe.xs("BMI Category", axis=1)[0]) == str


def test_build_dataframe5():
    assert type(completed_dataframe.xs("Health Risk", axis=1)[0]) == str


def test_get_weight_category_count1():
    assert get_weight_category_count(completed_dataframe, 'Overweight') == 1


def test_get_weight_category_count2():
    assert get_weight_category_count(completed_dataframe, 'Underweight') is None


def test_get_weight_category_count3():
    assert get_weight_category_count(completed_dataframe, 'Normal weight') == 2


def test_get_weight_category_count4():
    assert get_weight_category_count(completed_dataframe, 'Moderately obese') == 3


def test_get_weight_category_count5():
    assert get_weight_category_count(completed_dataframe, 'Severely obese') is None


def test_get_weight_category_count6():
    assert get_weight_category_count(completed_dataframe, 'Very severely obese') is None
