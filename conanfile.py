from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout, CMakeDeps
from conans.errors import ConanException
from conan.tools.scm import Git
import os

class scmRevisionRecipe(ConanFile):
    name = "scm_revision"
    version = "0.1"
    package_type = "application"

    # Optional metadata
    license = "<Put the package license here>"
    author = "<Put your name here> <And your email here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of scm_revision package here>"
    topics = ("<Put some tag here>", "<here>", "<and here>")

    # Binary configuration
    settings = "os", "compiler", "build_type", "arch"

    # Sources are located in the same place as this recipe, copy them to the recipe
    exports_sources = "CMakeLists.txt", "src/*", "data/gitRevision.cpp.in"
    
    def export(self):
        git = Git(self, self.recipe_folder)
        # save the url and commit in conandata.yml
        git.coordinates_to_conandata()

    def layout(self):
        cmake_layout(self)

    def generate(self):
        deps = CMakeDeps(self)
        deps.generate()
        tc = CMakeToolchain(self)
        tc.generate()
    
    def build(self):
        cmake = CMake(self)
        cmake_variables = { "scm_revision": self.conan_data["scm"]["commit"] }
        cmake.configure(variables=cmake_variables)
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()
