cmake_minimum_required(VERSION 3.00)

project(Lab)

add_library(StaticSource STATIC source/block.c)

add_library(SharedSource SHARED source/block.c)

# add the executable                                                          
add_executable(Shared program.c)
target_link_libraries(Shared SharedSource)

add_executable(Static program.c)
target_link_libraries(Static StaticSource)