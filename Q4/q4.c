#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>


int thread_count;	// 공유변수
char a[20]; //전달 메시지

void *Child_thread(void* rank);

int main(int argc, char *argv[])
{

	long thread;	// 쓰레드 변수
	pthread_t* thread_handles; //thread handler
	thread_count = strtol(argv[1], NULL, 10); //쓰레드 개수 받기
	thread_handles = malloc(thread_count *sizeof(pthread_t)); // 배열 생성

	printf("[ I'm Parent Thread ]\n");
	printf("Request Message : ");
	scanf("%s", a);
	
	for(thread=0; thread<thread_count; thread++)
		pthread_create(&thread_handles[thread], NULL, Child_thread, (void*)thread); // 자식 쓰레드 생성

	
	for(thread=0; thread<thread_count; thread++)
		pthread_join(thread_handles[thread], NULL); // 쓰레드 종료 및 함수 반환값

	free(thread_handles);
	return 0;	

}



void *Child_thread(void* rank)
{
	long my_rank=(long) rank;

	printf("\n[ I'm %ld child thread ] : %s\n", my_rank, a);
	return NULL;
}
