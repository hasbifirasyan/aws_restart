# Python3.6
# Coding: utf-8
# Store the human preproinsulin sequence in a variable called preproinsulin:
preproInsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktr" \
"reaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"

#remove the space between nucleid acid
preproInsulin = preproInsulin.replace(' ','')
print(f'preproInsulin: {preproInsulin}. length:{len(preproInsulin)}')

# Store the remaining sequence elements of human insulin in variables:
isInsulin=preproInsulin[0:24]
bInsulin=preproInsulin[24:54]
cInsulin=preproInsulin[54:89]
aInsulin=preproInsulin[89:110]

print(f'isInsulin: {isInsulin}. length: {len(isInsulin)}')
print(f'bInsulin: {bInsulin}. length: {len(bInsulin)}')
print(f'cInsulin: {cInsulin}. length: {len(cInsulin)}')
print(f'aInsulin: {aInsulin}. length: {len(aInsulin)}')

insulin = bInsulin + aInsulin
# Printing "the sequence of human insulin" to console using successive print() commands:
print("The sequence of human preproInsulin:")
print(preproInsulin)
# Printing to console using concatenated strings inside the print function (one-liner):
print("The sequence of human Insulin, chain a: " + aInsulin)
print(f'The sequence of human insulin, chain b: {bInsulin}')
print(insulin)

# Calculating the molecular weight of insulin  
# Creating a list of the amino acid (AA) weights  
aaWeights = {'A': 89.09, 'C': 121.16, 'D': 133.10, 'E': 147.13, 'F': 165.19,
'G': 75.07, 'H': 155.16, 'I': 131.17, 'K': 146.19, 'L': 131.17, 'M': 149.21,
'N': 132.12, 'P': 115.13, 'Q': 146.15, 'R': 174.20, 'S': 105.09, 'T': 119.12,
'V': 117.15, 'W': 204.23, 'Y': 181.19}  
print(f'aaWeights: {aaWeights}')

# Count the number of each amino acids  
aaCountInsulin = ({x: float(insulin.upper().count(x)) for x in ['A', 'C',
'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T',
'V', 'W', 'Y']})  
print(f'aaCountInsulin: {aaCountInsulin}')
# Multiply the count by the weights  
molecularWeightInsulin = sum({x: (aaCountInsulin[x]*aaWeights[x]) for x in
['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R',
'S', 'T', 'V', 'W', 'Y']}.values())  
print("The rough molecular weight of insulin: " +
str(molecularWeightInsulin))

molecularWeightInsulinActual = 5807.63
print("Error percentage: " + str(((molecularWeightInsulin - molecularWeightInsulinActual)/molecularWeightInsulinActual)*100))
