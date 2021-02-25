# Comandos básicos de Linux



### ls  

Lista el contenido de un directorio.  

```bash
$ ls 
$ ls -l 
$ ls -a 
$ ls -t 
$ ls -r
```



### cd 

Cambiar de directorio

```bash
$ cd <new dir>
$ cd ..
$ cd -
$ cd -t
$ cd -<username>
```



### pwd

Imprime la ruta actual

```bash
$ pwd
```



### mkdir

Crea un directorio nuevo tomando en cuenta la ubicación actual.

```bash
$ mkdir <dir name>
```



### touch

Se utiliza para crear archivos vacíos.

```bash
$ touch <nombre_del_archivo>
```

*Es una buena práctica incluir extensiones de tipo de archivo a los nombres de archivo.*



### cp

Este comando se usa para copiar un archivo o directorio.

```bash
$ cp <origen> <destino>
```



### mv

Mueve un archivo a una ruta específica, y a diferencia de cp, lo elimina del origen.

```bash
$ mv <origen> <destino>
```



### cat

muestra el contenido del archivo sin interrupción.

```bash
$ cat <archivo>     #Muestra el contenido en pantalla
$ cat <archivo> > <destino>   #envia el contenido de un archivo, hacia otro archivo, similar a cp
$ cat <archivo> >> <destino> #envia el contenido de un archivo y lo agrega en otro, conservando el contenido original del archivo destino.
```



### rm

Comando para borrar un archivo o directorio.

```bash
$ rm <archivo>
$ rm -r <nombre_directorio>
$ rmdir <nombre_directorio>  #solo funciona con directorios vacios
```



### sudo

Comando que permite a los usuarios ejecutar acciones con los privilegios de seguridad del root de manera segura.

```bash
$ sudo <comando_a_ejecutar>
```



### man

Con este comando puedes consultar las opciones disponibles para todos y cada uno de los comandos y aplicaciones disponibles

```bash
$ man <comando>
```



### clear

Limpia el contenido de la terminal

```bash
$ clear
```

