from fbs_runtime.application_context.PyQt5 import (ApplicationContext,
                                                   cached_property)


class AppContext(ApplicationContext):
    def run(self):
        return self.app.exec_()

    @cached_property
    def owl_pic(self):
        return self.get_resource('owl_3.png')