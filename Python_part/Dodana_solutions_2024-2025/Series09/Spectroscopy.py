def reference_spectra(file_path):
    spectra = {}
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split('\t')
            symbol = parts[0]
            wavelengths = tuple(sorted(map(float, parts[1].split(','))))
            spectra[symbol] = wavelengths
    return spectra

def reference_lines(measured, reference, eps=0.1):
    count = 0
    for ref_line in reference:
        if any(abs(ref_line - meas_line) <= eps for meas_line in measured):
            count += 1
    return count

def decomposition(measured, reference_spectra, eps=0.1, minimum=None):
    matching_elements = []
    for symbol, ref_spectrum in reference_spectra.items():
        matches = reference_lines(measured, ref_spectrum, eps=eps)

        if minimum is not None:
            if matches >= minimum:
                matching_elements.append(symbol)

        elif matches == len(ref_spectrum):
            matching_elements.append(symbol)

    return sorted(matching_elements)
