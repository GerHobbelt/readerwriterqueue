cmake_minimum_required(VERSION 3.9)
project(readerwriterqueue VERSION 0.0.99)

include(GNUInstallDirs)
include(CMakePackageConfigHelpers)

add_library(${PROJECT_NAME} INTERFACE)

target_include_directories(readerwriterqueue INTERFACE
                           "$<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}>"
                           "$<INSTALL_INTERFACE:include>"
)

install(FILES
        atomicops.h
        readerwriterqueue.h
    DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}/${PROJECT_NAME}
)
install(TARGETS readerwriterqueue
        EXPORT readerwriterqueueTargets
        INCLUDES DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}
)
install(EXPORT readerwriterqueueTargets
        FILE readerwriterqueueTargets.cmake
        NAMESPACE moodycamel::
        DESTINATION ${CMAKE_INSTALL_DATAROOTDIR}/cmake/readerwriterqueue
)

configure_package_config_file(${CMAKE_CURRENT_SOURCE_DIR}/Config.cmake.in
    "${CMAKE_CURRENT_BINARY_DIR}/readerwriterqueueConfig.cmake"
    INSTALL_DESTINATION ${CMAKE_INSTALL_DEFAULT_DATAROOTDIR}/cmake/readerwriterqueue
)
write_basic_package_version_file(
    "${CMAKE_CURRENT_BINARY_DIR}/readerwriterqueueConfigVersion.cmake"
    VERSION "${PROJECT_VERSION}"
    COMPATIBILITY AnyNewerVersion
)
install(FILES
        "${CMAKE_CURRENT_BINARY_DIR}/readerwriterqueueConfig.cmake"
        "${CMAKE_CURRENT_BINARY_DIR}/readerwriterqueueConfigVersion.cmake"
    DESTINATION ${CMAKE_INSTALL_DATAROOTDIR}/cmake/readerwriterqueue
)
