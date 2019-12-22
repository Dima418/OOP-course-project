from models.Developer import Developer


def main():
    dev = Developer('dev_fn_1', 'dev_ln_1', '1990/12/01')
    dev2 = Developer('dev_fn_2', 'dev_ln_2', '1999/10/01')
    dev3 = Developer(rnd=True)


if __name__ == "__main__":
    main()
