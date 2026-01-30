import { ThemedText } from '@/components/themed-text';
import { ThemedView } from '@/components/themed-view';
import { useColorScheme } from '@/hooks/use-color-scheme';
import { useThemeColor } from '@/hooks/use-theme-color';
export default function RoutineWidget() {
    const colorScheme = useColorScheme();
    const backgroundColor = useThemeColor(
        { light: '#fff3e8', dark: '#000846' },
        'background'
    );

    return <ThemedView style={[styles.container, { backgroundColor }]}>
            <ThemedText type="title">
                morning {"\n"}
                <ThemedText type="default">
                    7:00 AM - 8:00 AM
                </ThemedText>
            </ThemedText>
            <ThemedText type="default">
                M T W T F S S
            </ThemedText>
            
        </ThemedView>; 
}
const styles = {
    container: {
        padding: 16,
        borderRadius: 8,
        marginTop: 4,
        maginBottom:4,
        // Additional styling as needed
    },
};