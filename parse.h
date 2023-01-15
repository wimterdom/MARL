#include <stdio.h>
#include <libxml/parser.h>
#include <libxml/tree.h>
#include <stdlib.h>
#include <string.h>

#define parameter_array_size 100
#define parameter_strings_long 200
#define file_parameter_strings_long 200
#define variable_array_size 100
#define default_variable_num 100

struct parameter_list
{
    _Bool must;
    int count;
    char parameter[variable_array_size][parameter_strings_long];
};

char file_parameter[file_parameter_strings_long];
char parameter_index[variable_array_size][default_variable_num];
int para_index_table[variable_array_size][variable_array_size];
int must_index_table[default_variable_num];
struct parameter_list parameter[parameter_array_size];
int parameter_count;
int parameter_total; // total parameter count 

void parse_xml(char *xml_posion);
