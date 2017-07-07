set(MAC_EXECUTABLE mac-main)

add_executable(${MAC_EXECUTABLE} mac-main.mm)
target_link_libraries(${MAC_EXECUTABLE} ${PROJECT_NAME})

install(TARGETS ${MAC_EXECUTABLE} RUNTIME DESTINATION bin)

add_custom_target(run
  COMMAND ${MAC_EXECUTABLE}
  WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}/bin
)
