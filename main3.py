# Non-local variable-> Used inside nested functions to refer to a variables from outer function not global
# id()-> uique no to show where that value is stored in memory
# globals()-> show all global variables in program
# locals() -> show variables inside current function

x = "global_x"
print(f"[GLOBAL] Created x = '{x}', id = {id(x)}")

def outer():
    x = "outer_x"
    print(f"\n[OUTER] Created x = '{x}', id = {id(x)}")
    print("[OUTER] locals() ->", locals())   

    def inner(): 
        nonlocal x
        print(f"\n[INNER] Before change, x = '{x}', id = {id(x)}")
        x = "inner_modified_outer_x"
        print(f"[INNER] After change, x = '{x}', id = {id(x)}")
        print("[INNER] locals() ->", locals())

        def inner_most():
            x = "inner_most_x"
            print(f"\n[INNER-MOST] Created new x = '{x}', id = {id(x)}")
            print("[INNER-MOST] locals() ->", locals())

        inner_most()

    inner()
    
    print(f"\n[OUTER] After inner() call, x = '{x}', id = {id(x)}")
    print("[OUTER] locals() ->", locals())
outer()

print(f"\n[GLOBAL] After all functions, x = '{x}', id = {id(x)}")
print("[GLOBAL] globals()['x'] ->", globals()['x'])
