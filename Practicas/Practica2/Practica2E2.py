readme = '''NumPy is the fundamental package needed for scientific computing with Python.

Website: https://www.numpy.org
Documentation: https://numpy.org/doc
Mailing list: https://mail.python.org/mailman/listinfo/numpy-discussion
Source code: https://github.com/numpy/numpy
Contributing: https://www.numpy.org/devdocs/dev/index.html
Bug reports: https://github.com/numpy/numpy/issues
Report a security vulnerability: https://tidelift.com/docs/security
It provides:

a powerful N-dimensional array object
sophisticated (broadcasting) functions
tools for integrating C/C++ and Fortran code
useful linear algebra, Fourier transform, and random number capabilities
Testing:

NumPy requires pytest. Tests can then be run after installation with:

python -c 'import numpy; numpy.test()'
Call for Contributions
The NumPy project welcomes your expertise and enthusiasm!

Small improvements or fixes are always appreciated; issues labeled as "good first issue" may be a good starting point. If you are considering larger contributions to the source code, please contact us through the mailing list first.

Writing code isn’t the only way to contribute to NumPy. You can also:

review pull requests
triage issues
develop tutorials, presentations, and other educational materials
maintain and improve our website
develop graphic design for our brand assets and promotional materials
translate website content
help with outreach and onboard new contributors
write grant proposals and help with other fundraising efforts
If you’re unsure where to start or how your skills fit in, reach out! You can ask on the mailing list or here, on GitHub, by opening a new issue or leaving a comment on a relevant issue that is already open.

Our preferred channels of communication are all public, but if you’d like to speak to us in private first, contact our community coordinators at numpy-team@googlegroups.com or on Slack (write numpy-team@googlegroups.com for an invite).

We also have a biweekly community call, details of which are announced on the mailing list. You are very welcome to join.

If you are new to contributing to open source, this guide helps explain why, what, and how to successfully get involved.'''

punt = ''':/,-.'"()'''
for char in readme:
    if char in punt:
        readme = readme.replace(char, " ")  #Remplazando los caracteres especiales por espacios!

readmelst = readme.split()

readmeDict = {}

for word in readmelst:
    if word in readmeDict:
        readmeDict[word] += 1
    else:
        readmeDict[word] = 1

maxword = ""
maxvalue = -1
for key in readmeDict:
    if readmeDict[key] > maxvalue:
        maxvalue = readmeDict[key]
        maxword = key

print(f"La palbara mas repetid es: {maxword} y se repite: {maxvalue}")

#2. Indique la palabra que aparece mayor cantidad de veces en el texto del README.md de numpy.