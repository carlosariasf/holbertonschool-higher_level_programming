#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"
/**
* check_cycle - Find loop
* @list: Lista
* Return: 1 if loop 0 if not
**/

int check_cycle(listint_t *list)
{

	listint_t *fast = list;
	listint_t *slow = list;
	if(list == NULL)
		return (0);
	fast = fast->next;
	
	while (fast != NULL && fast->next != NULL && slow != NULL)
	{
		if (fast == slow)
			return (1);
	fast = fast->next->next;
	slow = slow->next;
	}		
	return (0);
}
