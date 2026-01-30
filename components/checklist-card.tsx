import { ThemedText } from '@/components/themed-text';
import { ThemedView } from '@/components/themed-view';
import { useColorScheme } from '@/hooks/use-color-scheme';
import { useThemeColor } from '@/hooks/use-theme-color';
import { Checkbox } from '@/node_modules/expo-checkbox';
import { useState } from 'react';
import { Collapsible } from './ui/collapsible';
export default function ChecklistCard() {
    const colorScheme = useColorScheme();
    const [isChecked, setChecked] = useState(false);

    const backgroundColor = useThemeColor(
        { light: '#fff3e8', dark: '#06f6f6ff' },
        'background'
    );

    return <Collapsible title="morning" style={[styles.container, { backgroundColor }]}>
            <ThemedView style={{flexDirection: 'row', alignItems: 'center', backgroundColor}}>
                <Checkbox style = {styles.checkbox} value={isChecked} onValueChange={setChecked} />
                <ThemedText type = 'default' style = {[styles.text]}> {" "}Normal checkbox</ThemedText>
            </ThemedView>
            
        </Collapsible>; 
}
const styles = {
    container: {
        padding: 16,
        borderRadius: 8,
        marginTop: 4,
        maginBottom:4,
        // Additional styling as needed
    },
    checkbox: {

    },
    text: {
        
    },
};