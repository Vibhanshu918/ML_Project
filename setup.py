from setuptools import find_packages,setup

#this setup function is just serving like meta data which will contain all the necessary informations about the author
#the reason behind this setup.py is I can build my entire machine learning application as a package and deploy it on pypi to let others use this as well by just installing it from there 
#or simply it's to building our application as a package
from typing import List
Hypen_e_dot='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    This function returns the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","")for req in requirements]   #this is just to replace an extra character i.e, \n by empty character
        if Hypen_e_dot in requirements:
            requirements.remove(Hypen_e_dot)
    return requirements

setup(
    name='ML Project',
    author_email='vkumarccmsd@gmail.com',
    version='0.0.1',
    author='Vibhanshu',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)