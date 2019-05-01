#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * insert_node - Inser node in sort linked list
 * @head: listint_t List
 * @number: Number to add
 * Return: moded listint_t
**/
listint_t *insert_node(listint_t **head, int number)
{
        listint_t *new;
        listint_t *current = *head;
        int index = 1;

        new = malloc(sizeof(listint_t));
        if (new == NULL)
                return (NULL);
        new->n = number;
	new->next = NULL;
	if (head == NULL || *head == NULL)
	{
		*head = new;
		return (new);
	}
	if (number < 0 && (*head)->n <= 0)
	{
		new->next = (*head);
		*head = new;
		return (new);
	}
	if (number < current->n && index == 1)
        {
		new->next = current;
		*head = new;
		return (new);
        }
        while (current->next != NULL && abs(number) >= abs(current->next->n))
      	{
		current = current->next;
		index++;
        }
	new->next = current->next;
	current->next = new;	
        
	return (new);
}
