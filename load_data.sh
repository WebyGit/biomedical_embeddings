#!/bin/bash

CURDIR="$(dirname $0)"

DATADIR=$CURDIR/data
RESULT_FILE=$DATADIR/all_texts.txt
UBER_RESULT_FILE=$DATADIR/all_texts_clean.txt
ARCHIVE_NAMES=`cat $CURDIR/archives.lst`
ARCHIVES_DIR=$DATADIR/archives

[ ! -d "$ARCHIVES_DIR" ] && mkdir -p "$ARCHIVES_DIR"
echo '' > "$RESULT_FILE"
echo '' > "$UBER_RESULT_FILE"

for arc in $ARCHIVE_NAMES
do
    echo Downloading $arc

    CUR_ARCHIVE_FILE=$ARCHIVES_DIR/$arc
    CUR_ARCHIVE_DIR=${CUR_ARCHIVE_FILE}_unpacked
    mkdir -p "$CUR_ARCHIVE_DIR"
    wget -O "$CUR_ARCHIVE_FILE" ftp://ftp.ncbi.nlm.nih.gov/pub/pmc/oa_bulk/$arc

    echo Unpacking $arc

    tar xf "$CUR_ARCHIVE_FILE" -C "$CUR_ARCHIVE_DIR"
    find "$CUR_ARCHIVE_DIR" -type f -name '*.txt' -exec cat {} \; >> "$RESULT_FILE"
    rm -r "$CUR_ARCHIVE_DIR" "$CUR_ARCHIVE_FILE"

    echo Done with $arc
done

echo Cleaning text
"$CURDIR/preprocess_text.py" "$RESULT_FILE" "$UBER_RESULT_FILE"