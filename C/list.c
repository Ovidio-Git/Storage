

#include <stdio.h>
#include <stdlib.h>


typedef struct{
	char data; 			 // Dato a almacenar en la lista
	struct ListNode *ptrnext; // Autoreferenciado de la estrucutra
} ListNode;

ListNode* header = NULL;
ListNode* footer = NULL;

ListNode* new(){
	ListNode* newptr = (ListNode*) malloc(sizeof(ListNode));
	newptr->ptrnext = NULL;
	return(newptr);
}

void insert(ListNode* node){

	if (header == NULL){
		header = node;
		footer = node;
	}
	else{
		footer->ptrnext = node;
		footer = node;
	}
}


int main (){
	ListNode* node = new();
	node->dato = 15;

	return 0;
}
