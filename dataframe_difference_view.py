from jinja2 import Environment, FileSystemLoader
from faker import Faker
from pandas import pandas

faker = Faker()

env = Environment(loader=FileSystemLoader('resources'))

expected = pandas.read_csv("expected_data.csv")
actual = pandas.read_csv("actual_data.csv")


def validate_data(expected_df, actual_df, reference_id):
    expected_df = expected_df.sort_values(by=reference_id).reset_index(drop=True)
    actual_df = actual_df.sort_values(by=reference_id).reset_index(drop=True)
    df_isin_results = expected_df.isin(actual_df)

    columns = df_isin_results.columns.values.tolist()
    differences = {}
    for value in columns:
        series = df_isin_results.index[df_isin_results[value] == False].tolist()
        expected_values = {}
        actual_values = {}
        for index in series:
            ref_id = expected_df[reference_id].values[index]
            expected_values[ref_id] = expected_df[value].values[index]
            actual_values[actual_df[reference_id].values[index]] = actual_df[value].values[index]
        if expected_values:
            differences[value] = {
                "expected": expected_values,
                "actual": actual_values
            }
    do_dataframes_match = df_isin_results.eq(True).all().all()
    print(differences)
    return do_dataframes_match, differences


if __name__ == '__main__':
    match, df_differences = validate_data(expected, actual, "id")
    if not match:
        parameters = {"df_differences": df_differences,
                      "reference_id": "id"}
        env.get_template("dataframe_difference_template.html", globals=parameters).stream(name='foo').dump('df_differences.html')
