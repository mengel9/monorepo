import { Regex } from '@monorepo/expo/shared/static';
import { DatePicker } from '@monorepo/expo/shared/ui-components';

interface IDateOfBirthPickerProps {
  value: Date | null | undefined;
  setValue: (date: Date) => void;
}

export default function DateOfBirthPicker(props: IDateOfBirthPickerProps) {
  const { value, setValue } = props;

  return (
    <DatePicker
      label="Date of Birth"
      disabled
      maxDate={new Date()}
      pattern={Regex.date}
      mode="date"
      format="MM/dd/yyyy"
      placeholder="MM/DD/YYYY"
      mt="xs"
      value={value || new Date()}
      setValue={setValue}
    />
  );
}