"""
=========================================================
 AEVRION Programming Language v0.4
 Environment System
=========================================================
"""


class Environment:


    def __init__(self, parent=None):

        # Store variables
        self.variables = {}

        # Parent scope
        self.parent = parent



    # =====================================================
    # Define Variable
    # =====================================================

    def define(self, name, value):

        self.variables[name] = value



    # =====================================================
    # Get Variable
    # =====================================================

    def get(self, name):

        if name in self.variables:

            return self.variables[name]


        if self.parent:

            return self.parent.get(name)


        raise Exception(
            f"Variable '{name}' is not defined"
        )



    # =====================================================
    # Update Variable
    # =====================================================

    def set(self, name, value):

        if name in self.variables:

            self.variables[name] = value
            return


        if self.parent:

            self.parent.set(name, value)
            return


        raise Exception(
            f"Variable '{name}' is not defined"
        )



    # =====================================================
    # Check Variable
    # =====================================================

    def exists(self, name):

        if name in self.variables:

            return True


        if self.parent:

            return self.parent.exists(name)


        return False



    # =====================================================
    # Remove Variable
    # =====================================================

    def delete(self, name):

        if name in self.variables:

            del self.variables[name]
            return


        if self.parent:

            self.parent.delete(name)
            return


        raise Exception(
            f"Variable '{name}' is not defined"
        )



    # =====================================================
    # Create Child Scope
    # =====================================================

    def create_child(self):

        return Environment(self)



    # =====================================================
    # Debug
    # =====================================================

    def show(self):

        return self.variables



    def __repr__(self):

        return (
            f"Environment({self.variables})"
        )

