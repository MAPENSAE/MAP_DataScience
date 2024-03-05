"""
Module: s3_fs

This module provides functions to import files and buckets from SSP (Secure and Scalable Platform)
cloud storage to the local system using the S3 protocol.

Usage:
    The module can be used to import files or entire buckets from SSP cloud storage to the local
    system.
"""

import os
import s3fs


def import_bucket_from_ssp_cloud(
    fs_obj, source_bucket_name, destination_folder, recursive=True
):
    """
    Import entire bucket from SSP cloud storage to local system.

    Args:
        fs_obj (s3fs.S3FileSystem): S3FileSystem object for accessing cloud storage.
        source_bucket_name (str): Name of the source bucket in the cloud storage.
        destination_folder (str): Path of the destination folder in the local system.
        recursive (bool, optional): Flag to indicate whether to import recursively or not. 
                                    Defaults to True.

    Raises:
        PermissionError: If user does not have the right permission to access the bucket.

    Returns:
        None
    """
    try:
        fs_obj.get(source_bucket_name, destination_folder, recursive=recursive)
        print(
            f"The bucket {source_bucket_name} has been downloaded to {destination_folder}"
        )
    except PermissionError:
        print(
            f"You tried to import {source_bucket_name} but you do not have the right permission"
            " to do so !"
        )


def import_file_from_ssp_cloud(fs_obj, source_file_name, destination_file_path):
    """
    Import a file from SSP cloud storage to local system.

    Args:
        fs_obj (s3fs.S3FileSystem): S3FileSystem object for accessing cloud storage.
        source_file_name (str): Name of the source file in the cloud storage.
        destination_file_path (str): Path of the destination file in the local system.

    Raises:
        PermissionError: If user does not have the right permission to access the file.
        FileNotFoundError: If the specified file does not exist in the cloud storage.

    Returns:
        None
    """
    try:
        fs_obj.get(source_file_name, destination_file_path)
        print(
            f"The file {source_file_name} has been downloaded to {destination_file_path}"
        )
    except PermissionError:
        print(
            f"You tried to import {source_file_name} but you do not have the right permission"
            " to do so !"
        )
    except FileNotFoundError:
        print(f"The file {source_file_name} does not exist")


if __name__ == "__main__":
    # Create filesystem object
    S3_ENDPOINT_URL = "https://" + os.environ["AWS_S3_ENDPOINT"]
    fs = s3fs.S3FileSystem(client_kwargs={"endpoint_url": S3_ENDPOINT_URL})

    # Example usage:
    import_bucket_from_ssp_cloud(fs, "maximerichaudeau1/data", "./data")
    import_bucket_from_ssp_cloud(fs, "maximerichaudeau1/json", "./json")
    import_file_from_ssp_cloud(
        fs,
        "maximerichaudeau1/cross_entropy_weighted10_batch64_32_16.pth",
        "./cross_entropy_weighted10_batch64_32_16.pth",
    )
    import_file_from_ssp_cloud(fs, "maximerichaudeau1/test.txt", "./test.txt")
