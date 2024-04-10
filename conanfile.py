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

    def layout(self):
        cmake_layout(self)

    def generate(self):
        deps = CMakeDeps(self)
        deps.generate()
        tc = CMakeToolchain(self)
        tc.generate()

    def find_git_commit(self):
        git = Git(self, self.recipe_folder)
        try:
            scm_revision = git.get_commit()
            if git.is_dirty():
                scm_revision += "-dirty"
        except ConanException:
            scm_revision = os.getenv("GIT_COMMIT")
            if scm_revision is None:
                scm_revision = "unknown"
        return scm_revision
    
    def build(self):
        scm_revision = self.find_git_commit()
        cmake = CMake(self)
        cmake_variables = { "scm_revision": scm_revision }
        cmake.configure(variables=cmake_variables)
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()
