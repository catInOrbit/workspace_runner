import logging
import os
import os.path

from action import do_action


logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)


def main() -> None:
    logger.info("with arguments:")
    for arg, val in sorted(args.items()):
        logger.info("  %s=%s:", arg, val)

    # Call the Action implementation.
    outputs = do_action(args)

    # export args to report folder
    export_args(args)

    # Print the outputs (which get picked up by GitHub Action Runners).
    for name, result in outputs.items():
        print(f"::set-output name={name}::{result}")


def export_args(args, file_name="run_args.txt"):
    with open(file_name, "w") as the_file:
        for key, value in args.items():
            the_file.write(f"{key} : {value}\n")
    os.chmod(file_name, 0o777)


if __name__ == "__main__":
    input_prefix = "INPUT_"
    args = {
        k[len(input_prefix) :].lower(): v
        for k, v in os.environ.items()
        if k.startswith(input_prefix)
    }
    main()
