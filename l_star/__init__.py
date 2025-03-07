alphabet = set('ab')

from l_star.teacher import Teacher

teacher = Teacher()

S: list = ['']  # prefixes (rows)
E: list = ['']  # postfixes (columns)

def l_star():
    from .__main__ import l_star as l_star_main
    l_star_main()

# Ensure that l_star is accessible at the package level
__all__ = ['l_star']
