from datascience import *
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plots
plots.style.use('fivethirtyeight')

# Create the initial table
# ds = Table().with_columns(
#     "Ho va Ten", make_array("Le Thi Ngheo", "Tran Van Kha", "Do Van Tam", "Nguyen Thi Binh", "Vo Van Giau", "Ly Thieu An"),
#     "Tuoi", make_array(17, 98, 52, 34, 62, 50),
#     "So Du (VND)", make_array(4.567E+5, 3.456E+7, 2.345E+6, 1.23E+7, 5.678E+9, 1.2e3)
# )

ds = Table().with_columns("Ho va Ten", make_array("đe Thi Ă", "Tran Van Đa", "Do Van de", "Nguyen Thi Binh", "Vo Van Giau", "Ly Thieu An"),
                          "Tuoi", make_array(17, 98, 52, 34, 62, 50),
                          "So Du (VND)", make_array(4.567E+5, 3.456E+7, 2.345E+6, 1.23E+7, 5.678E+9, 1.2e3))
print(ds)
print('--------------------------------------------------------------------------------------------------------------------------------------')


# Convert the values in the "So Du (VND)" column to fully formatted numbers
vnd = ds.apply(lambda x: "{:,.2f}".format(x), "So Du (VND)")

# Replace the "So Du (VND)" column with the newly formatted data
ds = ds.with_column("So Du (VND)", vnd)
print(ds)
print('--------------------------------------------------------------------------------------------------------------------------------------')


# Split names in the "Ho va Ten" column to extract the list of last names
ds_ten = ds.apply(lambda x: x.split()[-1], "Ho va Ten")

# Add a new column "Ten" from the extracted names
ds = ds.with_column("Ten", ds_ten)

# Sort the table by the "Ten" column and remove the "Ten" column
ds_sorted = ds.sort("Ten").drop("Ten")
print(ds_sorted)
print('--------------------------------------------------------------------------------------------------------------------------------------')


# Define the function for abbreviating names
def Ho_va_Ten(Ho_va_Ten):
    parts = Ho_va_Ten.split()
    ho_dem = parts[:-1]
    ten = parts[-1]
    viet_tat = ".".join([part[0] for part in ho_dem])
    return viet_tat + "." + ten

# Apply the abbreviation function and update the "Ho va Ten" column
ds_abbre = ds_sorted.apply(Ho_va_Ten, "Ho va Ten")
ds_sorted = ds_sorted.with_column("Ho va Ten", ds_abbre)

# Display the final sorted table
print(ds_sorted)
print('--------------------------------------------------------------------------------------------------------------------------------------')


vietnamese_alphabet = "aăâbcdđeêghiklmnopqrsotuưvxy"

def vietnamese_sort_key(name):
    name = name.lower()
    return [vietnamese_alphabet.index(char) if char in vietnamese_alphabet else ord(char) for char in name]

ten = ds.apply(lambda x: x.split()[-1],"Ho va Ten")
ds = ds.with_column("Ten", ten)

sorted_indices = sorted(range(len(ten)), key=lambda i: vietnamese_sort_key(ten[i]))

sortedvn_ds = ds.take(sorted_indices).drop('Ten')

print(sortedvn_ds)