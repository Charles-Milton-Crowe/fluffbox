

""" Just a couple internal utilites left here now."""


def Get_Letters(num):
    """ This func is given a number and returns that number with a few letters representing the
        place of the number(e.g. 1st, 2nd, etc)."""

    if num == 0:
    	return "{:>4}".format("VET")
    elif num == 1 or num % 10 == 1:
        if num == 11:
            return str("{:2}th".format(num))
        else:
            return str("{:2}st".format(num))
    elif num == 2 or num % 10 == 2:
        if num == 12:
            return str("{:2}th".format(num))
        else:
            return str("{:2}nd".format(num))
    elif num == 3 or num % 10 == 3:
        if num == 13:
            return str("{:2}th".format(num))
        else:
            return str("{:2}rd".format(num))
    elif num >= 4:
        return str("{:2}th".format(num))

def Load_Namefile(afile):
    with open(afile, 'r') as f:
        rows = f.readlines()

        for x in range(len(rows) - 1, -1, -1):
            if rows[x][0] == "\n" or rows[x][0] == "#":
                rows.pop(x)

    list = []
    for x in range(len(rows)):
        list.append(rows[x])
        list[-1] = list[-1].rstrip("\n")

    return list
