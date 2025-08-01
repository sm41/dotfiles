# check stdin
function check_stdin(){
  if   [[ -p /dev/stdin ]] ; then
    :
    # echo "# Input from pipe"
  elif [[ ! -p /dev/stdin ]] ; then
    echo "# function ERROR -> ${FUNCNAME[0]}"
    echo "# No input from pipe"
    show_usage
    exit 1
  fi
}

# $1 = number of target
# $2 = actual number
function check_number_of_argment(){
  if [[ "$1" != "$2" ]] ; then
    echo "# function ERROR -> ${FUNCNAME[0]}"
    show_usage
    exit 1
  fi
}

# check file contain
function check_empty_file(){
  if [[ ! -s "$1" ]] ; then
    echo ERROR!! $1 is Empty ; exit 1
  else
    sed -i 's/^$/d' "$1"
  fi
}