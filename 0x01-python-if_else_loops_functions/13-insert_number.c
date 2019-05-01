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
	listint_t *temp = *head;
	listint_t *current = *head;
	int index = 1;
	
	if (*head == NULL)
		return (NULL);
	temp = temp->next;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	while (current)
	{
		if (number < current->n && index == 1)
		{
			new->next = current;
			*head = new;
			return (new);
		}
		else if (number > current->n && number < temp->n && temp != NULL)
		{
			new->next = temp;
			current->next = new;
			return (new);
		}
		else if (temp == NULL)
		{
			current = current->next;
			current->next = new;
			return (new);
		}
	current = current->next;
	temp = temp->next;
	index++;
	}

	return (new);
}
